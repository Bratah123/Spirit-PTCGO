from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class _StageOneType(Passive):
    """Each of your Stage 1 Pokemon in play is now a Water Pokemon in addition to its types."""
    def modify_pokemon_types(self, types, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if (me is None or pokemon.owning_player_id != me.owning_player_id
                or pokemon.get_attribute(AttrID.STAGE) != PokemonStage.STAGE1.value
                or PokemonTypes.WATER.value in types):
            return types
        return list(types) + [PokemonTypes.WATER.value]


card = PokemonCardDef(
    guid="69b5ce39-396b-5b9a-83a6-1b450560212f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Aqua Effect",
            game_text="Each of your Stage 1 Pok\u00e9mon in play is now a Water Pok\u00e9mon in addition to its existing types.",
            passive=_StageOneType(),
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)