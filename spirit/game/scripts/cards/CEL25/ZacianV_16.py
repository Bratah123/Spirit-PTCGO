from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _is_psychic_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.PSYCHIC.value in types


card = PokemonCardDef(
    guid="a61f827e-fa94-56e2-9dab-cf53202828b1",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=16,
    set_code="CEL25",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Ability(
            title="Roar of the Sword",
            game_text="Once during your turn, you may search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=search_attach_energy(predicate=_is_psychic_energy_card, count=1, distribute=False),
        ),
        Attack(
            title="Storm Slash",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.PSYCHIC), 30, base=60),
        ),
    ],
)