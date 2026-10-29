from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.support_common import search_to_hand


card = PokemonCardDef(
    guid="a533657e-2f90-5a8f-8ba6-6199f518f53c",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_hand(is_supporter_card, count=1, reveal=True, prompt='Choose a Supporter card.'),
        ),
        Attack(
            title="Bright Horns",
            game_text="This Pok\u00e9mon can't use Bright Horns during your next turn.",
            cost={PokemonTypes.FAIRY: 3},
            damage=130,
            locks_next_turn=True,
        ),
    ],
)