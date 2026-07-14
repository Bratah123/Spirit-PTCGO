from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


class _IngotSwingShield(Passive):
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


async def ingot_swing(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _IngotSwingShield())


card = PokemonCardDef(
    guid="c6c77afc-4ec7-5cbf-88f7-62f24ec7a247",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1", "Single Strike", "Melmetal"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=189,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Ingot Swing",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon that have an Ability.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ingot_swing,
        ),
        Attack(
            title="Blasting Hammer",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)