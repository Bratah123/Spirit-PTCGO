from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import fling_away, mountain_smasher


card = PokemonCardDef(
    guid="670e39b1-2ace-5ac0-bca3-fd84f7a3a8af",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyranitar.Name",
    display_name="Dark Tyranitar",
    searchable_by=["Dark Tyranitar", "Stage 2", "DarkTyranitar"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Mountain Smasher",
            game_text="Flip a number of coins equal to the number of Fighting Energy cards attached to Dark Tyranitar. This attack does 20 damage times the number of heads. Then, for each heads, discard the top card from your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=mountain_smasher,
        ),
        Attack(
            title="Fling Away",
            game_text="If your opponent has any Benched Pok\u00e9mon, this attack does 30 damage instead of 50 and choose 1 of those Benched Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=fling_away,
        ),
    ],
)
