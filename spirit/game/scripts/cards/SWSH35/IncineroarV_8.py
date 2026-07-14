from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _is_benched(pokemon):
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


grand_flame = attach_from_discard(
    predicate=_is_fire_energy, count=2, target=_is_benched,
    prompt="Choose up to 2 Fire Energy cards to attach.",
)


card = PokemonCardDef(
    guid="85c3c274-ebeb-55ba-9399-6d0464feb806",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarV.Name",
    display_name="Incineroar V",
    searchable_by=["Incineroar V", "Basic", "V", "IncineroarV"],
    subtypes=["Basic", "V"],
    collector_number=8,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=727,
    abilities=[
        Attack(
            title="Grand Flame",
            game_text="Attach up to 2 Fire Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=grand_flame,
        ),
        Attack(
            title="Flare Blitzer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=recoil_attack(30),
        ),
    ],
)