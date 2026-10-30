from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.session.passives import carrier_pokemon
from spirit.game.session.effects import is_restored_pokemon


def _restored_ally(target, carrier):
    me = carrier_pokemon(carrier)
    return me is not None and target.owning_player_id == me.owning_player_id and is_restored_pokemon(target)


card = PokemonCardDef(
    guid="e15acfdc-cdc2-5218-a976-e76c0e61bcda",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith",
    searchable_by=["Anorith", "Restored", "Anorith"],
    subtypes=["Restored"],
    collector_number=56,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossilAnorith.Name",
    family_id=347,
    abilities=[
        Ability(
            title="Restored Barrier",
            game_text="Each of your Restored Pok\u00e9mon has no Weakness.",
            passive=no_weakness_passive(protects=_restored_ally),
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)