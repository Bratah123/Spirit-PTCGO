from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import is_pokemon_vmax


def _my_pokemon_in_play(carrier):
    holder = carrier_pokemon(carrier)
    if holder is None or holder.parent is None or holder.parent.parent is None:
        return []
    player_entity = holder.parent.parent
    result = []
    for area in player_entity.children:
        if area.get_attribute(AttrID.NAME) in ("activePokemonArea", "bench"):
            result.extend(area.children)
    return result


class MaximumDownerPassive(Passive):
    """If all your Pokemon in play are Fusion Strike, opposing Pokemon
    VMAX in play get -30 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or pokemon.owning_player_id == holder.owning_player_id:
            return 0
        if not is_pokemon_vmax(pokemon.archetype_id):
            return 0
        mine = _my_pokemon_in_play(carrier)
        if not mine or any("Fusion Strike" not in subtypes_for(p.archetype_id) for p in mine):
            return 0
        return -30


card = PokemonCardDef(
    guid="2fda4efc-1a09-53e0-aad6-54f3cbbf795b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Fusion Strike", "Toxtricity"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=108,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Ability(
            title="Maximum Downer",
            game_text="If all your Pokémon in play are Fusion Strike Pokémon, your opponent's Pokémon VMAX in play get -30 HP.",
            passive=MaximumDownerPassive(),
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
