from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class SwellingTunePassive(Passive):
    stacking_key = "SwellingTune"

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Kricketune":
            return 0
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value not in types:
            return 0
        return 40


card = PokemonCardDef(
    guid="5192187e-fe12-525b-8fb7-c6beffdc4049",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name",
    display_name="Kricketune",
    searchable_by=["Kricketune", "Stage 1", "Kricketune"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    family_id=401,
    abilities=[
        Ability(
            title="Swelling Tune",
            game_text="Your Grass Pokémon in play, except any Kricketune, get +40 HP. You can't apply more than 1 Swelling Tune Ability at a time.",
            passive=SwellingTunePassive(),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)