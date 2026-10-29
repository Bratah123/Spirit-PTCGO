from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import gale_shuriken
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="965fe9a0-2859-5ea2-8cfc-2163febed9ec",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    display_name="Frogadier",
    searchable_by=["Frogadier", "Stage 1", "Frogadier"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Gale Shuriken",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=gale_shuriken,
        ),
        Attack(
            title="Water Drip",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
