from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on
from spirit.game.card_effects.ecard import flame_vapor


card = PokemonCardDef(
    guid="99c2c542-a6f1-5396-a3d0-25d46f8e6d9e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Flame Vapor",
            game_text="When you play Gyarados from your hand to evolve your Active Pok\u00e9mon, you may flip 2 coins. For each heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=flame_vapor,
        ),
        Attack(
            title="Dragon's Vengeance",
            game_text="If Gyarados has 7 or more damage counters on it, this attack's base damage is 100.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=bonus_if(lambda ctx: damage_counters_on("self")(ctx) >= 7, 50),
        ),
    ],
)
