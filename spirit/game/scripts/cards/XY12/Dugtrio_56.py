from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="a4ce74b2-5f4c-587e-8558-18ed6ef56ba7",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Earthquake",
            game_text="This attack does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=spread_damage(20, side='mine', also_base=True),
        ),
    ],
)