from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _night_sight(ctx):
    """Once during your turn (before your attack), you may draw a card."""
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="ff0fdd93-db6f-5692-96c5-907745a63505",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Team Plasma", "Crobat"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=55,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Night Sight",
            game_text="Once during your turn (before your attack), you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=_night_sight,
        ),
        Attack(
            title="Ultra-Toxic Fang",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 4 damage counters instead of 1 on this Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.POISONED, counters=4),
        ),
    ],
)