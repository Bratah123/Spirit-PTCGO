from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import intimidate


card = PokemonCardDef(
    guid="2cc6ee6f-ca86-58ca-b0d1-e5b2b39b6439",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoking.Name",
    display_name="Giovanni's Nidoking",
    searchable_by=["Giovanni's Nidoking", "Stage 2", "GiovannisNidoking"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Intimidate",
            game_text="If the Defending Pok\u00e9mon's maximum HP is 50 or less, it can't attack Giovanni's Nidoking during your opponent's next turn. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.GRASS: 1},
            effect=intimidate,
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 30 more damage; if tails, this attack does 40 damage.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
