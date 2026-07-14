from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_energy_card


def _is_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


card = PokemonCardDef(
    guid="90f22b55-270b-53f4-8f60-26020942ee66",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaV.Name",
    display_name="Sandaconda V",
    searchable_by=["Sandaconda V", "Basic", "V", "SandacondaV"],
    subtypes=["Basic", "V"],
    collector_number=184,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=844,
    abilities=[
        Attack(
            title="Sand Eater",
            game_text="Attach a Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=attach_from_discard(
                predicate=_is_fighting_energy, count=1, target="self",
                prompt="Choose a Fighting Energy card to attach"),
        ),
        Attack(
            title="Sand Breath",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)