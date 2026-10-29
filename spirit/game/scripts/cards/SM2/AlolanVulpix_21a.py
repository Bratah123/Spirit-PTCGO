from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


card = PokemonCardDef(
    guid="69dae8d5-6f20-5c7a-ac6b-0c7aeb83ce4f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic", "AlolanVulpix"],
    subtypes=["Basic"],
    collector_number=171,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Attack(
            title="Beacon",
            game_text="Search your deck for up to 2 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=search_to_hand(is_pokemon_card, count=2, prompt='Choose up to 2 Pokémon to put into your hand.'),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)