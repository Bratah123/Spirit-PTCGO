from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


card = PokemonCardDef(
    guid="23466fee-b8c8-51c2-bad6-100dbaf9c1eb",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Team Plasma", "Durant"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=92,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(
            title="Call for Backup",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt="Choose a Pokémon"),
        ),
        Attack(
            title="Metal Jail",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)