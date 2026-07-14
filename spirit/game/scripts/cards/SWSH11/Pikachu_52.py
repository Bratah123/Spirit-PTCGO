from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import is_energy_card


def _pika_dash(pokemon, carrier):
    return pokemon is carrier and any(is_energy_card(c) for c in carrier.children)

card = PokemonCardDef(
    guid="53432f36-8edc-55f0-bcc6-052b1938bc91",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Ability(
            title="Pika Dash",
            game_text="If this Pok\u00e9mon has any Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_pika_dash),
        ),
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)