from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import ball_of_flame, hot_plate


card = PokemonCardDef(
    guid="d98f82a6-1051-5e84-ab42-3507c800e4b6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagcargo.Name",
    display_name="Dark Magcargo",
    searchable_by=["Dark Magcargo", "Stage 1", "DarkMagcargo"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Hot Plate",
            game_text="As long as Dark Magcargo is your Active Pok\u00e9mon, whenever a player puts a Baby Pok\u00e9mon or Basic Pok\u00e9mon onto his or her Bench from his or her hand, this power does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working if Dark Magcargo is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=hot_plate,
        ),
        Attack(
            title="Ball of Flame",
            game_text="You may discard a Fire Energy card attached to Dark Magcargo when you use this attack. If you do and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=ball_of_flame,
        ),
    ],
)
