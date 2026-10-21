from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.passives_common import raise_defender_attack_cost_next_turn


async def _cyber_crush(ctx):
    """Discard all Special Energy attached to each of your opponent's Pokemon."""
    await ctx.deal_damage()
    cards = [e for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
             for e in ctx.attached_energies(p) if is_special_energy(e)]
    if cards:
        await ctx.discard_cards(cards)


card = PokemonCardDef(
    guid="47bbaaa2-458d-5d97-8b6b-1b95095fa168",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Cyber Crush",
            game_text="Discard all Special Energy attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_cyber_crush,
        ),
        Attack(
            title="Slowing Beam",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=raise_defender_attack_cost_next_turn(1),
        ),
    ],
)