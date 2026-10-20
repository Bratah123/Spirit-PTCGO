from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.passives import Passive, carrier_pokemon


class _StageOneType(Passive):
    """Each of your Stage 1 Pokemon in play is now a Fire Pokemon in addition to its types."""
    def modify_pokemon_types(self, types, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if (me is None or pokemon.owning_player_id != me.owning_player_id
                or pokemon.get_attribute(AttrID.STAGE) != PokemonStage.STAGE1.value
                or PokemonTypes.FIRE.value in types):
            return types
        return list(types) + [PokemonTypes.FIRE.value]


card = PokemonCardDef(
    guid="f84611cc-0cd0-5516-bf79-3c2ebb4b90da",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Flare Effect",
            game_text="Each of your Stage 1 Pok\u00e9mon in play is now a Fire Pok\u00e9mon in addition to its existing types.",
            passive=_StageOneType(),
        ),
        Attack(
            title="Heat Breath",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)