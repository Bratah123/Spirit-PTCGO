from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

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
            game_text="Your Grass Pok\u00e9mon in play, except any Kricketune, get +40 HP. You can't apply more than 1 Swelling Tune Ability at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)