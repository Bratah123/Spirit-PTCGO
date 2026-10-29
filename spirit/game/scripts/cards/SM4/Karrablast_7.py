from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import has_shelmet_in_hand, shell_on

card = PokemonCardDef(
    guid="f73fad69-6778-54dd-9ab2-42aaa900f5c7",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Ability(
            title="Shell On",
            game_text="Once during your turn (before your attack), you may discard a Shelmet from your hand. If you do, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=shell_on,
            activation=Activations.ONCE_PER_TURN,
            condition=has_shelmet_in_hand,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)