from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import relaxing_scent


card = PokemonCardDef(
    guid="ca520bf9-62df-5bc0-97aa-dc3d6017dc2e",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasIvysaur.Name",
    display_name="Erika's Ivysaur",
    searchable_by=["Erika's Ivysaur", "Stage 1", "ErikasIvysaur"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBulbasaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Relaxing Scent",
            game_text="As long as Erika's Ivysaur is your Active Pok\u00e9mon, whenever an attack (even your own) does damage to any Pok\u00e9mon (after applying Weakness and Resistance), that attack only does half the damage to that Pok\u00e9mon (rounded up to the nearest 10). (Any other effects of attacks still happen.) This power stops working while Erika's Ivysaur is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=relaxing_scent,
        ),
        Attack(
            title="Double Razor Leaf",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 3},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)
