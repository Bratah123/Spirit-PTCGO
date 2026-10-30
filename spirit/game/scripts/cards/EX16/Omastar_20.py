from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import extra_energy_damage, pull_down


card = PokemonCardDef(
    guid="e4a4c875-7638-5497-bb86-6a0396c6a00a",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Pull Down",
            game_text="If your opponent has any Evolved Pok\u00e9mon in play, remove the highest Stage Evolution card from each of them and put those cards back into his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pull_down,
        ),
        Attack(
            title="Hydrocannon",
            game_text="Does 30 damage plus 20 more damage for each Water Energy attached to Omastar but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=extra_energy_damage(
                20, base=30, extra_cap=2, energy_type=PokemonTypes.WATER,
            ),
        ),
    ],
)
