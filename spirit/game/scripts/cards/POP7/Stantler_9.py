from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import lead_search_supporter, frighten_horn_confuse_basic

card = PokemonCardDef(
    guid="cebaf604-0e05-55ba-92f3-6d140cf1501b",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=['Stantler', 'Basic', 'Stantler'],
    subtypes=["Basic"],
    collector_number=9,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=lead_search_supporter(),
        ),
        Attack(
            title="Frighten Horn",
            game_text="If the Defending Pokémon isn't an Evolved Pokémon, that Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=frighten_horn_confuse_basic(20),
        ),
    ],
)
