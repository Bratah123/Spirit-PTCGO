from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="901c7740-3b1a-5b7e-a902-2aedf07ff052",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name",
    display_name="Diggersby",
    searchable_by=["Diggersby", "Stage 1", "Diggersby"],
    subtypes=["Stage 1"],
    collector_number=147,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    family_id=659,
    abilities=[
        Attack(
            title="Mining Rush",
            game_text="Discard up to 6 cards from the top of your deck. If you do, this attack does 30 damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 4},
            damage=110,
        ),
    ],
)