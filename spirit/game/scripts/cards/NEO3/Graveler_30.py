from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.ecard import rock_tumble


card = PokemonCardDef(
    guid="aef0bf25-16ac-5002-ac72-d5d27ca1860a",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=spread_damage(10, side='mine', also_base=True),
        ),
        Attack(
            title="Rock Tumble",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            effect=rock_tumble,
        ),
    ],
)
