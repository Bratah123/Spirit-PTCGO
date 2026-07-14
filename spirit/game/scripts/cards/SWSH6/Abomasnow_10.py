from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class ToughnessBoostPassive(Passive):
    """Your Single Strike Pokemon (except any Abomasnow) get +50 HP."""

    stacking_key = "ToughnessBoost"

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        pdef = def_for(pokemon.archetype_id)
        if pdef is not None and pdef.name.endswith("pokemon.Abomasnow.Name"):
            return 0
        if "Single Strike" not in subtypes_for(pokemon.archetype_id):
            return 0
        return 50


card = PokemonCardDef(
    guid="8ac70bbc-422e-568d-90f0-d3d358fb423f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Single Strike", "Abomasnow"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=10,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Ability(
            title="Toughness Boost",
            game_text="Your Single Strike Pok\u00e9mon in play, except any Abomasnow, get +50 HP. You can't apply more than 1 Toughness Boost Ability at a time.",
            passive=ToughnessBoostPassive(),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)