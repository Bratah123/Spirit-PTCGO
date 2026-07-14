from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class _SnowMirageShield(Passive):
    """Prevent all damage from an opposing attacker with an Ability."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.target is carrier):
            return False
        attacker = calc.attacker
        if attacker is None:
            return False
        return any(
            isinstance(entry, dict) and entry.get("abilityType") != "Attack"
            for entry in (attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
        )


async def snow_mirage(ctx):
    """160, ignoring effects on the opponent's Active. Shield this Pokemon from
    Ability-Pokemon attacks during your opponent's next turn."""
    await ctx.deal_damage(ignore_target_effects=True)
    ctx.add_passive_through_opponents_turn(ctx.attacker, _SnowMirageShield())


async def silvery_snow_star(ctx):
    """70 for each of the opponent's Pokemon V in play; not affected by W/R."""
    count = sum(1 for p in ctx.opponent_pokemon_in_play() if is_pokemon_v(p.archetype_id))
    await ctx.deal_damage(70 * count, apply_modifiers=False)

card = PokemonCardDef(
    guid="728c4d6d-24df-58ab-9e66-535803077792",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpixVSTAR.Name",
    display_name="Alolan Vulpix VSTAR",
    searchable_by=["Alolan Vulpix VSTAR", "VSTAR", "AlolanVulpixVSTAR"],
    subtypes=["VSTAR"],
    collector_number=197,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpixV.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Snow Mirage",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon that have an Ability.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=snow_mirage,
        ),
        Attack(
            title="Silvery Snow Star",
            game_text="This attack does 70 damage for each of your opponent's Pok\u00e9mon V in play. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={},
            damage=70,
            damage_operator="x",
            vstar=True,
            effect=silvery_snow_star,
        ),
    ],
)