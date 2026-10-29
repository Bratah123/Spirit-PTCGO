from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sl import JungleTotemPassive

card = PokemonCardDef(
    guid="f77be2dd-6f59-52ef-b41d-863a8f84ebf7",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Jungle Totem",
            game_text="Each basic Grass Energy attached to your Pok\u00e9mon provides GrassGrass Energy. You can't apply more than 1 Jungle Totem Ability at a time.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=JungleTotemPassive(),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)