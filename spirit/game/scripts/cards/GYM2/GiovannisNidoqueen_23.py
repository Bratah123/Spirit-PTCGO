from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, flip_or_nothing
from spirit.game.card_effects.ecard import named_on_bench


card = PokemonCardDef(
    guid="ebd5a316-8347-59a4-bae8-4da0220b761c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoqueen.Name",
    display_name="Giovanni's Nidoqueen",
    searchable_by=["Giovanni's Nidoqueen", "Stage 2", "GiovannisNidoqueen"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Love Lariat",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 50 more damage if you have at least 1 Giovanni's Nidoking on your Bench. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_or_nothing(
                then=bonus_if(named_on_bench("Giovanni's Nidoking"), 50),
            ),
        ),
    ],
)
