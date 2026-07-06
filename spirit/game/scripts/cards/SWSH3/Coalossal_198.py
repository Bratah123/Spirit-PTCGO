from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d0c3b8c3-ddb7-5d04-881c-0dc286bddc2f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2", "Coalossal"],
    subtypes=["Stage 2"],
    collector_number=198,
    set_code="SWSH3",
    rarity=Rarities.RareSecret,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=839,
    abilities=[
        Ability(
            title="Tar Generator",
            game_text="Once during your turn, you may attach a Fire Energy card, a Fighting Energy card, or 1 of each from your discard pile to your Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Flaming Avalanche",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)