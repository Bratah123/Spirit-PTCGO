from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_pokemon_card

card = PokemonCardDef(
    guid="69cc4221-e5ce-5117-bde6-9124d404682b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    display_name="Mareanie",
    searchable_by=["Mareanie", "Basic", "Mareanie"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=747,
    abilities=[
        Attack(
            title="Bail Out",
            game_text="Put a Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(is_pokemon_card, count=1, minimum=0, prompt='Choose a Pokémon to put into your hand'),
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)