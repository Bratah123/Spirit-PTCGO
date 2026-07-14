from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_discount
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _has_fire_energy(pokemon, carrier):
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return any(
        energy_provides_type(e, PokemonTypes.FIRE.value)
        for e in pokemon.children if is_energy_card(e)
    )


card = PokemonCardDef(
    guid="0c345c2e-ac3b-5a35-a963-e80bf2b4d5c7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Byway of the Nine-Tailed Fox",
            game_text="The Retreat Cost of each of your Pok\u00e9mon that has any Fire Energy attached is ColorlessColorless less.",
            passive=retreat_discount(2, target_pred=_has_fire_energy),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)