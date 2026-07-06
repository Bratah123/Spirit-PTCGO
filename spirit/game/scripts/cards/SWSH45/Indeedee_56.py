from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db0d3387-b717-5dcf-8dd3-afede27df122",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic", "Indeedee"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SWSH45",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Attack(
            title="Helping Hand",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Benched Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)