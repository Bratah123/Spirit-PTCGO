from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2470d314-35d8-54be-b8c4-3f0f504f0765",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Sun Energy",
            game_text="Once during your turn, you may attach a Psychic Energy card from your discard pile to 1 of your Lunatone.",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)