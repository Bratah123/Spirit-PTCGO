from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="9c80065c-34da-5684-8f79-c21bdd53fa71",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Magnitude",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=spread_damage(10, side="both", also_base=True),
        ),
    ],
)
