from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.attacks_common import damage_per


def _grass_fairy(ctx):
    return sum(1 for p in ctx.my_pokemon_in_play()
               if {PokemonTypes.GRASS.value, PokemonTypes.FAIRY.value}
               & set(p.get_attribute(AttrID.POKEMON_TYPES) or []))


card = PokemonCardDef(
    guid="03f7a0e9-3f22-5771-ae19-dbe5c94384cf",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesEX.Name",
    display_name="Florges-EX",
    searchable_by=["Florges-EX", "Basic", "EX", "FlorgesEX"],
    subtypes=["Basic", "EX"],
    collector_number=116,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=671,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_to_hand(is_supporter_card, count=1, reveal=True, prompt='Choose a Supporter card'),
        ),
        Attack(
            title="Bright Garden",
            game_text="This attack does 20 damage times the number of Grass Pok\u00e9mon and Fairy Pok\u00e9mon you have in play.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(_grass_fairy, 20),
        ),
    ],
)