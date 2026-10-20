from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="57eed303-2a46-56fd-b93e-76fe4698745c",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Pile Up",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon Tool card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)