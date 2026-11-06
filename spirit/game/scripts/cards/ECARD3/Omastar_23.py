from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import PrimalStarePassive


card = PokemonCardDef(
    guid="583fb371-373e-5de5-ba8e-a38f168c1f50",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Primal Stare",
            game_text="As long as Omastar is your Active Pok\u00e9mon, your opponent can't play Basic Pok\u00e9mon or Evolution cards from his or her hand to evolve his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=PrimalStarePassive(),
        ),
        Attack(
            title="Spook",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
