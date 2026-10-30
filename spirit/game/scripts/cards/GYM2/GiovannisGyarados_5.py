from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import dragon_tornado, summon_storm


card = PokemonCardDef(
    guid="ea6135b6-a9d5-507b-bff8-9565ff30bb89",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisGyarados.Name",
    display_name="Giovanni's Gyarados",
    searchable_by=["Giovanni's Gyarados", "Stage 1", "GiovannisGyarados"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMagikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Summon Storm",
            game_text="Flip 2 coins. If both of them are heads, this attack does 20 damage to each other Pok\u00e9mon (even your own). Don't apply Weakness and Resistance for this attack.",
            cost={PokemonTypes.WATER: 1},
            effect=summon_storm,
        ),
        Attack(
            title="Dragon Tornado",
            game_text="Unless this attack Knocks Out the Defending Pok\u00e9mon, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=dragon_tornado,
        ),
    ],
)
