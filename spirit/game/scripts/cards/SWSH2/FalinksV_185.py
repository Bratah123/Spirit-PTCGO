from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive


def _protects_falinks(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    definition = def_for(target.archetype_id)
    return bool(definition and "falinks" in (definition.display_name or "").lower())


card = PokemonCardDef(
    guid="45ad3075-16d0-5034-9fe7-ca8a81419e83",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FalinksV.Name",
    display_name="Falinks V",
    searchable_by=["Falinks V", "Basic", "V", "FalinksV"],
    subtypes=["Basic", "V"],
    collector_number=185,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Ability(
            title="Iron Defense Formation",
            game_text="All of your Pok\u00e9mon that have \"Falinks\" in their name take 20 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_protects_falinks),
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)