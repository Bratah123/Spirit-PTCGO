from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import look_for_friends

card = PokemonCardDef(
    guid="e6cd41fc-0ddb-58b7-8ef4-a1b0a2fd6c8e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran \u2640", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Look for Friends",
            game_text="Reveal cards from your deck until you reveal a Basic Pok\u00e9mon. Show that card to your opponent and put it into your hand. Shuffle the other revealed cards into your deck. (If you don't reveal a Basic Pok\u00e9mon, shuffle all the revealed cards back into your deck.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=look_for_friends(),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)