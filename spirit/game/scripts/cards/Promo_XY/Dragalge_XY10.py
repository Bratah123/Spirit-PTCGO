from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import no_retreat_passive


def _opposing_poisoned(pokemon, carrier):
    if pokemon.owning_player_id == carrier.owning_player_id:
        return False
    return CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] in (
        pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="28114aec-8b71-55a4-ad24-f9d093f71a4e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1", "Dragalge"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Ability(
            title="Poison Barrier",
            game_text="Your opponent's Poisoned Pok\u00e9mon can't retreat.",
            passive=no_retreat_passive(_opposing_poisoned),
        ),
        Attack(
            title="Poison Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)