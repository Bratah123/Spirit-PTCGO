from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22334d1c-3802-58c1-905e-9ac81dbb1183",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Telekinesis",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dream Waltz",
            game_text="This attack can be used even if this Pok\u00e9mon is Asleep. If this Pok\u00e9mon is Asleep, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)