from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import downpour, downpour_condition, riptide


card = PokemonCardDef(
    guid="7bd86a11-5a2e-5f07-bc9e-2f9740e412bf",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Downpour",
            game_text="As often as you like during your turn (before your attack), you may discard a Water Energy card from your hand. This power can't be used if Feraligatr is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=downpour_condition,
            effect=downpour,
        ),
        Attack(
            title="Riptide",
            game_text="Does 10 damage plus 10 damage times the number of Water Energy cards in your discard pile. Then, shuffle all Water Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.WATER: 3},
            damage=10,
            damage_operator="+",
            effect=riptide,
        ),
    ],
)
