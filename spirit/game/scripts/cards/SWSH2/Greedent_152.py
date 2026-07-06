from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d771e6d9-7c9b-5807-9b5e-85d63c498dd1",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1", "Greedent"],
    subtypes=["Stage 1"],
    collector_number=152,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Ability(
            title="Greedy Tail",
            game_text="Once during your turn, you may search your deck for a Pok\u00e9mon Tool card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)