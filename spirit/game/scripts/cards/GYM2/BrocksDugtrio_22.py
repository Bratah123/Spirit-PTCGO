from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.ecard import used_named_attack_last_turn


card = PokemonCardDef(
    guid="d723e281-e8a5-5994-a922-cab886e22d34",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksDugtrio.Name",
    display_name="Brock's Dugtrio",
    searchable_by=["Brock's Dugtrio", "Stage 1", "BrocksDugtrio"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksDiglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Lie Low",
            game_text="All damage done to Brock's Dugtrio during your opponent's next turn is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Earthdrill",
            game_text="This attack can't be used unless Brock's Dugtrio used its Lie Low attack last turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            condition=used_named_attack_last_turn("Lie Low"),
        ),
    ],
)
