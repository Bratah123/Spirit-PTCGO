from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import mist_guard, wondrous_gift

card = PokemonCardDef(
    guid="9692db09-a72d-573f-a910-379b826a0b5b",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2", "Florges"],
    subtypes=["Stage 2"],
    collector_number=86,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Wondrous Gift",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, put an Item card from your discard pile on top of your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=wondrous_gift,
        ),
        Attack(
            title="Mist Guard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Dragon Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=mist_guard,
        ),
    ],
)
