from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import evolve_self_from_deck

card = PokemonCardDef(
    guid="038d596b-ae25-517a-87e6-b77560e2737c",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1", "Gabite"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=evolve_self_from_deck,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)