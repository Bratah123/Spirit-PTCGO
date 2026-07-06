from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2d9bd21-030a-5bcd-887e-93db6255c9cb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wyrdeer.Name",
    display_name="Wyrdeer",
    searchable_by=["Wyrdeer", "Stage 1", "Wyrdeer"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    family_id=234,
    abilities=[
        Ability(
            title="Hurried Gait",
            game_text="Once during your turn, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)