from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, recoil_attack
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER)

card = PokemonCardDef(
    guid="a6ba6ab5-9512-50b2-b521-e393e041a8eb",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KinglerV.Name",
    display_name="Kingler V",
    searchable_by=["Kingler V", "Basic", "V", "KinglerV"],
    subtypes=["Basic", "V"],
    collector_number=28,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=99,
    abilities=[
        Attack(
            title="Falling Bubbles",
            game_text="Flip a coin. If heads, search your deck for up to 5 Water Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=flip_or_nothing(then=search_attach_energy(_is_water_energy, count=5)),
        ),
        Attack(
            title="Raging Pincer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=recoil_attack(30),
        ),
    ],
)