from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import takes_less_passive


def _is_dragon(pokemon):
    return PokemonTypes.DRAGON.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="14b805a3-9860-5e1c-b8ca-df2ba4b47988",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Spirit Charm",
            game_text="All of your Pok\u00e9mon take 30 less damage from attacks from your opponent's Dragon Pok\u00e9mon (after applying Weakness and Resistance). You can't apply more than 1 Spirit Charm Ability at a time.",
            passive=takes_less_passive(
                30, protects="team", attacker_pred=_is_dragon, stack_key="SpiritCharm"
            ),
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)